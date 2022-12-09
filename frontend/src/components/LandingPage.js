import * as React from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import Button from "@mui/material/Button";
import { useState } from "react";
import { CryptographyScannerApi } from "../api/CryptographyScannerApi";
import { useNavigate } from "react-router-dom";

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
        <Grid container alignItems="center" justifyContent="center">
            <Grid item>
                <Box
                    component="img"
                    sx={{
                        height: 200,
                        width: 200,
                        maxHeight: { xs: 200, md: 200 },
                        maxWidth: { xs: 200, md: 200 },
                    }}
                    alt="cyberark logo"
                    src="https://avatars.githubusercontent.com/u/30869256?s=280&v=4"
                />
                <Typography variant="h3" gutterBottom>
                    CyberArk Cryptography Scanner
                </Typography>
            </Grid>
            <Grid item container justifyContent="center">
                <div>
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
                            onChange={(e) => setOrganization(e.target.value)}
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
                </div>
            </Grid>
            <Grid item>
                <Button variant="contained" onClick={() => handleSubmit()}>
                    Scan
                </Button>
            </Grid>
        </Grid>
    );
}
