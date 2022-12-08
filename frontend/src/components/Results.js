import * as React from "react";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import EnhancedTable from "./ResultsTable";
import Box from "@mui/material/Box";
import { ResultsContext, UserIdContext } from "../App";
import { CryptographyScannerApi } from "../api/CryptographyScannerApi";
import { useEffect } from "react";

export default function Results() {
    const { userId, setUserId } = React.useContext(UserIdContext);
    const { results, setResults } = React.useContext(ResultsContext);

    const getResults = () => {
        console.log("in get results");
        CryptographyScannerApi()
            .getResults(userId)
            .then((res) => {
                console.log("in get results", res.data.results);
                if (res.data !== null) {
                    setResults(res.data.results);
                } else {
                    setInterval(getResults, 3000);
                }
            });
    };
    useEffect(() => {
        getResults();
    }, []);

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
