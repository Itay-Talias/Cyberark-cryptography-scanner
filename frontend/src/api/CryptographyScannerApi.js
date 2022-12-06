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

    return { scan };
}