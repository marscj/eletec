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

export function Info() {
  return axios({
    url: api.Info,
    method: "get"
  });
}
