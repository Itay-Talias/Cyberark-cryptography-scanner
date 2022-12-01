import * as React from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";

function createData(algorithm, keyLength, location, category) {
    return { algorithm, keyLength, location, category };
}

const rows = [
    createData("Frozen yoghurt", 159, 6.0, "Hash"),
    createData("Ice cream sandwich", 237, 9.0, "Hash"),
    createData("Eclair", 262, 16.0, "Hash"),
    createData("Cupcake", 305, 3.7, "Hash"),
    createData("Gingerbread", 356, 16.0, "Hash"),
];

export default function Results() {
    return (
        <Grid container alignItems="center" justifyContent="center">
            <Grid item>
                <Typography variant="h3" gutterBottom>
                    CyberArk Cryptography Scanner
                </Typography>
            </Grid>
            <TableContainer component={Paper}>
                <Table sx={{ minWidth: 650 }} aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell>Algorithm</TableCell>
                            <TableCell align="right">Key length</TableCell>
                            <TableCell align="right">Location</TableCell>
                            <TableCell align="right">Hash/encryption</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {rows.map((row) => (
                            <TableRow
                                key={row.name}
                                sx={{
                                    "&:last-child td, &:last-child th": {
                                        border: 0,
                                    },
                                }}
                            >
                                <TableCell component="th" scope="row">
                                    {row.algorithm}
                                </TableCell>
                                <TableCell align="right">
                                    {row.keyLength}
                                </TableCell>
                                <TableCell align="right">
                                    {row.location}
                                </TableCell>
                                <TableCell align="right">
                                    {row.category}
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </Grid>
    );
}
