import * as React from "react";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import EnhancedTable from "./ResultsTable";
import Box from '@mui/material/Box';

export default function Results() {
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
            <EnhancedTable></EnhancedTable>
        </Grid>
    );
}