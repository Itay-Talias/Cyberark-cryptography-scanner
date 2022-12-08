import axios from "axios";
import constants from "../constants";

export function CryptographyScannerApi() {
    function scan(organization, token) {
        return axios.post(constants.SCAN_API, {
            organization: organization,
            token: token,
            vcs_type: "github",
        });
    }
    function getResults(userId) {
        return axios.get(constants.GET_RESULTS_API, { withCredentials: true });
    }

    return { scan, getResults };
}
