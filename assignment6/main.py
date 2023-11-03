import requests
import json

# Lintcode API endpoint to scrape question data
BASE_URL = "https://apiv1.lintcode.com/v2/api/problems/{}"

#Serverless function endpoint
POST_URL = "https://addquestion-repgsbwosq-uc.a.run.app"

def fetch_data(number):
    response = requests.get(BASE_URL.format(number))
    data = response.json()

    # Extract required fields from the JSON
    desc = data.get("data", {}).get("description", "")
    example = data.get("data", {}).get("example", "")
    description = desc + "\n\n" + example
    level = data.get("data", {}).get("level", "")
    name = data.get("data", {}).get("problem_type_tag", {}).get("name", "")
    title = data.get("data", {}).get("title", "")

    return description, level, name, title

def title_to_slug(title):
    # Remove certain characters like '+'
    title = title.replace('+', '')
    
    # Convert to lowercase, replace spaces with hyphens and remove non-alphanumeric characters
    slug = ''.join(e for e in title if e.isalnum() or e.isspace()).lower()
    slug = slug.replace(' ', '-')
    
    return slug

def send_to_serverless_function(data):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(POST_URL, data=json.dumps(data), headers=headers)
    return response.status_code

def main():
    for i in range(1, 3001):
        try:
            description, complexity, categories, title = fetch_data(i)
            slug = title_to_slug(title)
            if complexity <= 1:
                complexity = 1
            elif complexity == 2:
                complexity = 2
            elif complexity >= 3:
                complexity = 3

            # Create the link to the actual problem
            PROBLEM_LINK = "https://www.lintcode.com/problem/{}"
            link = PROBLEM_LINK.format(i)
            data = {
                "category": categories,
                "complexity": complexity,
                "description": description,
                "link": link,  # Link to the problem
                "slug": slug,
                "title": title
            }
            
            # Send data as POST request to the serverless function
            response_status = send_to_serverless_function(data)
            if response_status == 200:
                print(f"Data for problem {i} sent successfully!")
            else:
                print(f"Failed to send data for problem {i}.")
            
        except Exception as e:
            # Fail silently and continue with the next iteration
            print(e)
if __name__ == "__main__":
    main()