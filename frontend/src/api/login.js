import api from "./index";
import { axios } from "@/utils/request";

export function login(parameter) {
  return axios({
    url: "/auth/login",
    method: "post",
    data: parameter
  });
}
