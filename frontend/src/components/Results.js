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
                    src="https://www.cyberark.com/wp-content/uploads/2021/01/cyberark-logo-dark.svg"
                />
                <Typography variant="h3" gutterBottom className="title-result">
                    Cryptography Scanner
                </Typography>
            </Grid>
            <EnhancedTable></EnhancedTable>
        </Grid>
    );
}
