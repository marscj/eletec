import {
  API,
  updateSuccess,
  createSuccess,
  deleteSuccess,
  deleteFailed,
  createFailed,
  updateFailed
} from "./index";
import { axios } from "@/utils/request";

export function getApplications(parameter) {
  return axios({
    url: API.Applications,
    method: "get",
    params: parameter
  });
}

export function getApplication(pk) {
  return axios({
    url: API.Applications + `${pk}/`,
    method: "get"
  });
}

export function updateApplication(pk, data) {
  return axios({
    url: API.Applications + `${pk}/`,
    method: "put",
    data: data
  })
    .then(updateSuccess)
    .catch(updateFailed);
}

export function createApplication(data) {
  return axios({
    url: API.Applications,
    method: "post",
    data: data
  })
    .then(createSuccess)
    .catch(createFailed);
}

export function deleteApplication(pk) {
  return axios({
    url: API.Applications + `${pk}/`,
    method: "delete"
  })
    .then(deleteSuccess)
    .catch(deleteFailed);
}
