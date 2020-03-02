import { API } from "./index";
import { axios } from "@/utils/request";

export function phoneGenerate(parameter) {
  return axios({
    url: API.Generate,
    method: "post",
    data: parameter
  });
}

export function phoneValidate(parameter) {
  return axios({
    url: API.Validate,
    method: "post",
    data: parameter
  });
}

export function getInfo() {
  return axios({
    url: API.Info,
    method: "get"
  });
}

export function logout() {
  return axios({
    url: API.Logout,
    method: "get"
  });
}
