import * as React from "react";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import EnhancedTable from "./ResultsTable";
import Box from "@mui/material/Box";
import { ResultsContext } from "../App";
import { CryptographyScannerApi } from "../api/CryptographyScannerApi";
import { useEffect, useState } from "react";
import "../style/Results.css";

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
                              scanStatus: "success",
                              url: file["url"].concat(
                                  "#L",
                                  file["algorithms"][index]["line_index"]
                              ),
                          };
                      });
                  } else if (!file["success"]) {
                      return {
                          category: "n/a",
                          library: "n/a",
                          repo: file["location"]["repo"],
                          path: file["location"]["path"],
                          algorithm: "n/a",
                          keyLength: "n/a",
                          line: "n/a",
                          scanStatus: "failed",
                          url: file["url"],
                      };
                  } else if (file["algorithms"].length == 0) {
                      return {
                          category: file["category"],
                          library: file["library"],
                          repo: file["location"]["repo"],
                          path: file["location"]["path"],
                          algorithm: "None",
                          keyLength: "n/a",
                          line: "n/a",
                          scanStatus: "success",
                          url: file["url"],
                      };
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
                    setTimeout(getResults, 3000);
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
            <EnhancedTable rows={rows}></EnhancedTable>
        </Grid>
    );
}
