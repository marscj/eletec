import api from "./index";
import { axios } from "@/utils/request";

export function getGroups(parameter) {
  return axios({
    url: api.Groups,
    method: "get",
    params: parameter
  });
}

export function getGroup(pk) {
  return axios({
    url: api.Groups + `${pk}/`,
    method: "get"
  });
}

export function updateGroup(pk, data) {
  return axios({
    url: api.Groups + `${pk}/`,
    method: "put",
    data: data
  });
}

export function createGroups(data) {
  return axios({
    url: api.Groups,
    method: "post",
    data: data
  });
}

export function getPermissions(parameter) {
  return axios({
    url: api.Permissions,
    method: "get",
    params: parameter
  });
}

export function getPermission(pk) {
  return axios({
    url: api.Permissions + `${pk}/`,
    method: "get"
  });
}

export function updatePermission(pk, data) {
  return axios({
    url: api.Permissions + `${pk}/`,
    method: "put",
    data: data
  });
}

export function createPermission(data) {
  return axios({
    url: api.Permissions,
    method: "post",
    data: data
  });
}
