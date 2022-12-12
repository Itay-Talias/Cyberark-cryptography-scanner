import * as React from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import Button from "@mui/material/Button";
import { useState, useEffect } from "react";
import { CryptographyScannerApi } from "../api/CryptographyScannerApi";
import { useNavigate } from "react-router-dom";
import "../style/LandingPage.css";
import { useCookies } from "react-cookie";

export default function LandingPage() {
    const [cookies, setCookie] = useCookies(["scan_id"]);
    const [organization, setOrganization] = useState("");
    const [token, setToken] = useState("");
    const navigate = useNavigate();
    useEffect(() => {
        let expires = new Date();
        expires.setTime(expires.getTime() + 560 * 1000);
        setCookie("scan_id", "", {
            path: "/",
            expires,
        });
    }, []);

    function handleSubmit() {
        CryptographyScannerApi()
            .scan(organization, token)
            .then((res) => {
                let expires = new Date();
                expires.setTime(expires.getTime() + 560 * 1000);
                setCookie("scan_id", res.data.id.toString(), {
                    path: "/",
                    expires,
                });
                if (res.status === 200) {
                    navigate("/results");
                } else {
                    window.alert("Connection failed");
                }
            });
    }

    return (
        <div className="container-login">
            <Grid container alignItems="center">
                <Grid item xs={6} className="left-box">

                    <Typography
                        variant="h1"
                        gutterBottom
                        className="title-prod"
                    >
                        Cryptography Scanner
                    </Typography>
                </Grid>
                <Grid item justifyContent="center" className="right-box">
                    <div className="login-box">
                        <Box
                            sx={{
                                width: 350,
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
                                width: 350,
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
