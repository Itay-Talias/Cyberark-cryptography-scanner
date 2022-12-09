import * as React from "react";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import EnhancedTable from "./ResultsTable";
import Box from "@mui/material/Box";
import { ResultsContext, UserIdContext } from "../App";
import { CryptographyScannerApi } from "../api/CryptographyScannerApi";
import { useEffect, useState } from "react";

function createData(results) {
    const rows =
        results.length > 0
            ? results.map((file) => {
                  if (file["success"] && file["algorithms"].length > 0) {
                      return file["algorithms"].map((line, index) => {
                          return {
                              category: file["category"],
                              library: file["library"],
                              repo: file["location"]["repo"],
                              path: file["location"]["path"],
                              algorithm: file["algorithms"][index]["word"],
                              keyLength: file["algorithms"][index]["key_size"],
                              line: file["algorithms"][index]["line_index"],
                          };
                      });
                  }
              })
            : [];
    const res = rows.flat(1).filter((element) => {
        return element !== undefined;
    });
    return res;
}

export default function Results() {
    const [rows, setRows] = useState([]);
    const { results, setResults } = React.useContext(ResultsContext);

    const getResults = () => {
        const scan_id = localStorage.getItem("scan_id");
        CryptographyScannerApi()
            .getResults(scan_id)
            .then((res) => {
                if (res?.data?.results) {
                    setResults(res.data.results);
                    setRows(createData(res.data.results));
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
            <EnhancedTable rows={rows}></EnhancedTable>
        </Grid>
    );
}
