import api from "./index";
import { axios } from "@/utils/request";

export function getUsers(parameter) {
  return axios({
    url: api.Users,
    method: "get",
    params: parameter
  });
}

export function getUser(pk) {
  return axios({
    url: api.Users + `${pk}/`,
    method: "get"
  });
}

export function updateUser(pk, data) {
  return axios({
    url: api.Users + `${pk}/`,
    method: "put",
    data: data
  });
}
