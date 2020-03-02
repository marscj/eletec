import {
  API,
  updateSuccess,
  createSuccess,
  deleteSuccess,
  deleteFailed
} from "./index";
import { axios } from "@/utils/request";

export function getGroups(parameter) {
  return axios({
    url: API.Groups,
    method: "get",
    params: parameter
  });
}

export function getGroup(pk) {
  return axios({
    url: API.Groups + `${pk}/`,
    method: "get"
  });
}

export function updateGroup(pk, data) {
  return axios({
    url: API.Groups + `${pk}/`,
    method: "put",
    data: data
  }).then(updateSuccess);
}

export function createGroups(data) {
  return axios({
    url: API.Groups,
    method: "post",
    data: data
  }).then(createSuccess);
}

export function getPermissions(parameter) {
  return axios({
    url: API.Permissions,
    method: "get",
    params: parameter
  });
}

export function getPermission(pk) {
  return axios({
    url: API.Permissions + `${pk}/`,
    method: "get"
  });
}

export function updatePermission(pk, data) {
  return axios({
    url: API.Permissions + `${pk}/`,
    method: "put",
    data: data
  }).then(updateSuccess);
}

export function createPermission(data) {
  return axios({
    url: API.Permissions,
    method: "post",
    data: data
  }).then(createSuccess);
}
