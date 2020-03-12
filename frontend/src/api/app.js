import {
  API,
  deleteSuccess,
  deleteFailed,
  createSuccess,
  createFailed
} from "./index";
import { axios } from "@/utils/request";

export function getApps(parameter) {
  return axios({
    url: API.Apps,
    method: "get",
    params: parameter
  });
}

export function getApp(pk, data) {
  return axios({
    url: API.Apps + `${pk}/`,
    method: "put",
    data: data
  });
}

export function createApp(data) {
  return axios({
    url: API.Apps,
    method: "post",
    data: data
  })
    .then(createSuccess)
    .catch(createFailed);
}

export function deleteApp(pk) {
  return axios({
    url: API.Apps + `${pk}/`,
    method: "delete"
  })
    .then(deleteSuccess)
    .catch(deleteFailed);
}
