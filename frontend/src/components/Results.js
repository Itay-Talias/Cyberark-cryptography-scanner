import * as React from "react";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import EnhancedTable from "./ResultsTable";

export default function Results() {
    return (
        <Grid container alignItems="center" justifyContent="center">
            <Grid item>
                <Typography variant="h3" gutterBottom>
                    CyberArk Cryptography Scanner
                </Typography>
            </Grid>
            <EnhancedTable></EnhancedTable>
        </Grid>
    );
}