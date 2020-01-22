import api from "./index";
import { axios } from "@/utils/request";

export function phoneGenerate(parameter) {
  return axios({
    url: api.Generate,
    method: "post",
    data: parameter
  });
}

export function phoneValidate(parameter) {
  return axios({
    url: api.Validate,
    method: "post",
    data: parameter
  });
}

export function getInfo() {
  return axios({
    url: api.Info,
    method: "get"
  });
}

export function logout() {
  return axios({
    url: api.Logout,
    method: "get"
  });
}
