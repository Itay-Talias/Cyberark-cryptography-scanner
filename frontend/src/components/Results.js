import * as React from "react";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import EnhancedTable from "./ResultsTable";
import Box from "@mui/material/Box";
import "../style/Results.css";

export default function Results() {
    return (
        <Grid container alignItems="center" justifyContent="center">
            <Grid item>
                <Box
                    component="img"
                    sx={{
                        height: 100,
                        width: 200,
                    }}
                    alt="cyberark logo"
                    src="https://images.g2crowd.com/uploads/product/image/social_landscape/social_landscape_a1ff161ba2b69dfe821e2c53d0e3b958/cyberark-privileged-access-manager.png
                    "
                />
                <Typography variant="h3" gutterBottom className="title-result">
                    Cryptography Scanner
                </Typography>
            </Grid>
            <EnhancedTable></EnhancedTable>
        </Grid>
    );
}
