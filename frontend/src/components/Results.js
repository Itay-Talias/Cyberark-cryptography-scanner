import * as React from "react";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import EnhancedTable from "./ResultsTable";
import Box from "@mui/material/Box";
import { ResultsContext } from "../App";
import { CryptographyScannerApi } from "../api/CryptographyScannerApi";
import { useEffect, useState } from "react";
import "../style/Results.css";
import Divider from "@mui/material/Divider";
import HighlightOffOutlinedIcon from "@mui/icons-material/HighlightOffOutlined";
import CheckCircleOutlineOutlinedIcon from "@mui/icons-material/CheckCircleOutlineOutlined";
import { green, red } from "@mui/material/colors";

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
                          category: "",
                          library: "",
                          repo: file["location"]["repo"],
                          path: file["location"]["path"],
                          algorithm: "syntax error",
                          keyLength: "",
                          line: "",
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
        CryptographyScannerApi()
            .getResults()
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
        <Grid container justifyContent="center">
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
                    <Typography
                        variant="h3"
                        gutterBottom
                        className="title-result"
                    >
                        Cryptography Scanner
                    </Typography>
                </Grid>
            </Grid>
            <Grid
                xs={2}
                sx={{ m: "1rem", ml:"87rem" }}
                display="flex"
                justifyContent="flex-end"
            >
                <Grid item xs={6} display="flex" justifyContent="flex-center">
                    <CheckCircleOutlineOutlinedIcon
                        sx={{
                            color: green[500],
                            mr: "0.5rem",
                        }}
                    />
                    scan success
                </Grid>
                {/* <Divider orientation="vertical" flexItem /> */}
                <Grid item xs={6} display="flex" justifyContent="flex-center">
                    <HighlightOffOutlinedIcon
                        sx={{
                            color: red[500],
                            mr: "0.5rem",
                        }}
                    />
                    scan failed
                </Grid>
            </Grid>
            <EnhancedTable rows={rows}></EnhancedTable>
        </Grid>
    );
}
