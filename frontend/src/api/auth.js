import { API } from "./index";
import { axios } from "@/utils/request";

export function phoneGenerate(data) {
  return axios({
    url: API.Generate,
    method: "post",
    data: data
  });
}

export function phoneValidate(data) {
  return axios({
    url: API.Validate,
    method: "post",
    data: data
  });
}

export function emailValidate(data) {
  return axios({
    url: API.EmailValidate,
    method: "post",
    data: data
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
