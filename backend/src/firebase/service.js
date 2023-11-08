// import { firebaseDB } from "./module";
import {
  collection,
  getDocs,
  getDoc,
  addDoc,
  updateDoc,
  deleteDoc,
  doc,
} from "firebase/firestore/lite";
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore/lite";
import dotenv from "dotenv";

dotenv.config();

const firebaseConfig = {
  apiKey: process.env.apiKey,
  authDomain: process.env.authDomain,
  projectId: process.env.projectId,
  storageBucket: process.env.storageBucket,
  messagingSenderId: process.env.senderId,
  appId: process.env.appId,
  measurementId: process.env.measurementId,
};

const app = initializeApp(firebaseConfig);
export const firebaseDB = getFirestore(app);

// Get all questions from DB
export async function getAllQuestions() {
  const questionsCol = collection(firebaseDB, "questions");
  const questionSnapshot = await getDocs(questionsCol);
  const questionList = questionSnapshot.docs.map((doc) => doc.data());
  return questionList;
}

export async function addQuestion(questionData) {
  const questionsCol = collection(firebaseDB, "questions");
  const docRef = await addDoc(questionsCol, questionData);
  return docRef._key.path.segments[1];
}

export async function updateQuestionById(uuid, updatedData) {
  const questionDoc = doc(firebaseDB, "questions", uuid);
  await updateDoc(questionDoc, updatedData);
}

export async function deleteQuestionById(uuid) {
  const questionDoc = doc(firebaseDB, "questions", uuid);
  await deleteDoc(questionDoc);
}

export async function getQuestionById(uuid) {
  const questionDoc = doc(firebaseDB, "questions", uuid);
  const docSnapshot = await getDoc(questionDoc);
  if (docSnapshot.exists()) {
    return docSnapshot.data();
  } else {
    return null;
  }
}
