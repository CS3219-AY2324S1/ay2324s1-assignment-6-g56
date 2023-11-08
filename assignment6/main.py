import asyncio
import time
import aiohttp
import json
from categories import categories_list

# Lintcode API endpoint to scrape question data
BASE_URL = "https://apiv1.lintcode.com/v2/api/problems/{}"

# Lintcode question URL
QUESTION_URL = "https://www.lintcode.com/problem/{}"

#Serverless function endpoint
POST_URL = "https://addquestion-repgsbwosq-uc.a.run.app"

categories_set = set(categories_list)

async def fetch_data(number, session: aiohttp.ClientSession):
    link = BASE_URL.format(number)
    try:
        async with session.get(url=link) as response:
            data = await response.json()
            
            if not data.get("data"):
                raise Exception(f"Problem {number} not found!")

            # Extract required fields from the JSON
            desc = data.get("data", {}).get("description", "")
            example = data.get("data", {}).get("example", "")
            description = desc + "\n\n" + example
            level = data.get("data", {}).get("level", "")
            tags = list(map(lambda tag: tag.get("name", ""), data.get("data", {}).get("tags", {})))
            title = data.get("data", {}).get("title", "")
            slug = data.get("data", {}).get("unique_name", "")
            
            if level < 1:
                level = 1
            elif level > 3:
                level = 3
            
            categories = list(filter(lambda x: x in categories_set, tags))
            categories = list(map(lambda x: "Mathematics" if x == "Mathmatics" else x, categories))
            if not categories:
                print(f"Problem {number} has no category. Skipping...")
                return
            
            data = {
                "categories": categories,
                "difficulty": level,
                "description": description,
                "link": QUESTION_URL.format(number), # Link to the problem
                "slug": slug,
                "title": title
            }
            
            # Send data as POST request to the serverless function
            response_status = await send_to_serverless_function(data, session)
            if response_status == 200:
                print(f"Data for problem {number} sent successfully!")
            else:
                print(f"Failed to send data for problem {number}.")
            
    except Exception as e:
        print(e)

async def send_to_serverless_function(data, session: aiohttp.ClientSession):
    headers = {
        "Content-Type": "application/json"
    }
    async with session.post(POST_URL, data=json.dumps(data), headers=headers) as response:
        return response.status

async def main():
    async with aiohttp.ClientSession() as session:
        ret = await asyncio.gather(*[fetch_data(i, session) for i in range(1, 3746)])
        print("Pulled {} outputs.".format(len(ret)))

if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    print("Took {} seconds to pull {} websites.".format(time.perf_counter() - start, 3745))