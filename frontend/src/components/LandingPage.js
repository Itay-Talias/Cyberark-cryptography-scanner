import * as React from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import Button from "@mui/material/Button";
import { useState } from "react";
import { CryptographyScannerApi } from "../api/CryptographyScannerApi";
import { useNavigate } from "react-router-dom";
import "../style/LandingPage.css";

export default function LandingPage() {
    const [organization, setOrganization] = useState("");
    const [token, setToken] = useState("");
    const navigate = useNavigate();

    function handleSubmit() {
        CryptographyScannerApi()
            .scan(organization, token)
            .then((res) => {
                localStorage.setItem("scan_id", res.data.id.toString());
                return res;
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
                            width: 870,
                        }}
                        alt="cyberark logo"
                        src="https://www.cyberark.com/wp-content/uploads/2021/01/cyberark-logo-dark.svg"
                    />
                    <Typography
                        variant="h1"
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
