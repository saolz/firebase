import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
    apiKey: "AIzaSyACsV5B2Ir5YF4u72WfiwGydhd4Ib5p0NE",
    authDomain: "zsaa-b4dc5.firebaseapp.com",
    projectId: "zsaa-b4dc5",
    storageBucket: "zsaa-b4dc5.firebasestorage.app",
    messagingSenderId: "759233918023",
    appId: "1:759233918023:web:027404eef2525c3f312d62",
    measurementId: "G-JBCQEZQFTS"
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);

