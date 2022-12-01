import * as React from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";

export default function LandingPage() {
    return (
        <Grid container alignItems="center" justifyContent="center">
            <Grid item>
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
                            id="token"
                            margin="normal"
                        />
                    </Box>
                </div>
            </Grid>
        </Grid>
    );
}
