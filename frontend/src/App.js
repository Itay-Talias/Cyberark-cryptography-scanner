import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LandingPage from "./components/LandingPage";
import Results from "./components/Results";

function App() {
    return (
        <div className="App">
            <Router>
                <Routes>
                    <Route path="/" element={<LandingPage />} />
                    <Route path="/results" element={<Results />} />
                </Routes>
            </Router>
        </div>
    );
}

export default App;
