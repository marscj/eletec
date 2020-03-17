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

export function getJobs(parameter) {
  return axios({
    url: API.Jobs,
    method: "get",
    params: parameter
  });
}

export function getJob(pk) {
  return axios({
    url: API.Jobs + `${pk}/`,
    method: "get"
  });
}

export function updateJob(pk, data) {
  return axios({
    url: API.Jobs + `${pk}/`,
    method: "put",
    data: data
  })
    .then(updateSuccess)
    .catch(updateFailed);
}

export function createJob(data) {
  return axios({
    url: API.Jobs,
    method: "post",
    data: data
  })
    .then(createSuccess)
    .catch(createFailed);
}

export function deleteJob(pk) {
  return axios({
    url: API.Jobs + `${pk}/`,
    method: "delete"
  })
    .then(deleteSuccess)
    .catch(deleteFailed);
}
