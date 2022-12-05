import "./App.css";
import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LandingPage from "./components/LandingPage";
import Results from "./components/Results";

export const ResultsContext = React.createContext([]);

function App() {
    const [results, setResults] = useState([]);
    return (
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
    );
}

export default App;
