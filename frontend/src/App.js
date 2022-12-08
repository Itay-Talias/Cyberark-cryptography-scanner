import "./App.css";
import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LandingPage from "./components/LandingPage";
import Results from "./components/Results";
import { useCookies } from "react-cookie";

export const UserIdContext = React.createContext("");
export const ResultsContext = React.createContext([]);

function App() {
    const [results, setResults] = useState([]);
    const [userId, setUserId] = useState("");

    return (
        <UserIdContext.Provider value={{ userId, setUserId }}>
            <ResultsContext.Provider value={{ results, setResults }}>
                <div className="App">
                    <Router>
                        <Routes>
                            <Route path="/" element={<LandingPage />} />
                            <Route path="/results" element={<Results />} />
                        </Routes>
                    </Router>
                </div>
            </ResultsContext.Provider>
        </UserIdContext.Provider>
    );
}

export default App;
