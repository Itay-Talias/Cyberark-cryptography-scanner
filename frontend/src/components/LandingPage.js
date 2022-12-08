import * as React from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import Button from "@mui/material/Button";
import { useState } from "react";
import { CryptographyScannerApi } from "../api/CryptographyScannerApi";
import { ResultsContext } from "../App";
import { useNavigate } from "react-router-dom";
import "../style/LandingPage.css";

export default function LandingPage() {
    const [organization, setOrganization] = useState("");
    const [token, setToken] = useState("");
    const { results, setResults } = React.useContext(ResultsContext);
    const navigate = useNavigate();
    function handleSubmit() {
        CryptographyScannerApi()
            .scan(organization, token)
            .then((res) => {
                setResults(res.data);
            });
        navigate("/results");
    }

    return (
        <div className="container-login">
            <Grid container alignItems="center">
                <Grid item xs={6} className="left-box">
                    <Box
                        component="img"
                        sx={{
                            height: 220,
                            width: 470,
                        }}
                        alt="cyberark logo"
                        src="https://images.g2crowd.com/uploads/product/image/social_landscape/social_landscape_a1ff161ba2b69dfe821e2c53d0e3b958/cyberark-privileged-access-manager.png
                    "
                    />
                    <Typography
                        variant="h2"
                        gutterBottom
                        className="title-prod"
                    >
                        Cryptography Scanner
                    </Typography>
                </Grid>
                <Grid item justifyContent="center" xs={6} className="right-box">
                    <div className="login-box">
                        <Box
                            sx={{
                                width: 500,
                                maxWidth: "100%",
                            }}
                        >
                            <TextField
                                fullWidth
                                label="organization"
                                id="organization"
                                margin="normal"
                                onChange={(e) =>
                                    setOrganization(e.target.value)
                                }
                            />
                        </Box>
                        <Box
                            sx={{
                                width: 500,
                                maxWidth: "100%",
                            }}
                        >
                            <TextField
                                fullWidth
                                label="token"
                                type="password"
                                id="token"
                                margin="normal"
                                onChange={(e) => setToken(e.target.value)}
                            />
                        </Box>
                        <Button
                            className="btn-login"
                            variant="contained"
                            onClick={() => handleSubmit()}
                        >
                            Scan
                        </Button>
                    </div>
                </Grid>
            </Grid>
        </div>
    );
}
