// question is a JSON object
const createQuestion = (question) => {
    const questions = getQuestions();
    if (Object.keys(questions).length === 0) {
        const id = 1;
        question.questionId = id;
        questions[id] = question;
        localStorage.setItem("questions", JSON.stringify(questions));
        return;
    }
    // basic error handling to check for duplicates
    questionTitles = Object.values(questions).map((question) => question.questionTitle);
    if (questionTitles.includes(question.questionTitle)) {
        throw new Error("Question already exists");
    }
    const id = parseInt(Object.keys(questions)[-1]) + 1; // sets id to the next available id
    question.questionId = id;
    questions[id] = question;
    localStorage.setItem("questions", JSON.stringify(questions));
};

const getQuestionById = (id) => {
    const questions = getQuestions();
    return questions[id];
};

const getQuestions = () => {
    const questions = JSON.parse(localStorage.getItem("questions"));
    return questions;
};

const deleteQuestionById = (id) => {
    const questions = getQuestions();
    delete questions[id];
    localStorage.setItem("questions", JSON.stringify(questions));
};

const testing = () => {
    localStorage.setItem("questions", JSON.stringify({}));
    const sampleQuestion = {
            questionTitle: "Reverse a String",
            questionDescription: 
            `Write a function that reverses a string. The input string is given as an array 
            of characters s. 
            
            You must do this by modifying the input array in-place with O(1) extra 
            memory. 
            
            
            Example 1: 
            
            Input: s = ["h","e","l","l","o"] 
            Output: ["o","l","l","e","h"] 
            Example 2: 
            
            Input: s = ["H","a","n","n","a","h"] 
            Output: ["h","a","n","n","a","H"] 
            
            Constraints: 
            
            1 <= s.length <= 105
            s[i] is a printable ascii character`,
            questionCategories: ["String", "Algorithms"],
            questionComplexity: "Easy",
    };

    createQuestion(sampleQuestion);
    console.log(getQuestions());
}