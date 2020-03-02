import {
  API,
  updateSuccess,
  createSuccess,
  deleteSuccess,
  deleteFailed
} from "./index";
import { axios } from "@/utils/request";

export function getUsers(parameter) {
  return axios({
    url: API.Users,
    method: "get",
    params: parameter
  });
}

export function getUser(pk) {
  return axios({
    url: API.Users + `${pk}/`,
    method: "get"
  });
}

export function updateUser(pk, data) {
  return axios({
    url: API.Users + `${pk}/`,
    method: "put",
    data: data
  }).then(updateSuccess);
}

export function getContract(parameter) {
  return axios({
    url: API.Contracts,
    method: "get",
    params: parameter
  });
}

export function updateContract(pk, data) {
  return axios({
    url: API.Contracts + `${pk}/`,
    method: "put",
    data: data
  }).then(updateSuccess);
}

export function createContract(data) {
  return axios({
    url: API.Contracts,
    method: "post",
    data: data
  }).then(createSuccess);
}

export function deleteContract(pk) {
  return axios({
    url: API.Contracts + `${pk}/`,
    method: "delete"
  })
    .then(deleteSuccess)
    .catch(deleteFailed);
}

export function getAddress(parameter) {
  return axios({
    url: API.Address,
    method: "get",
    params: parameter
  });
}

export function updateAddress(pk, data) {
  return axios({
    url: API.Address + `${pk}/`,
    method: "put",
    data: data
  }).then(updateSuccess);
}

export function createAddress(data) {
  return axios({
    url: API.Address,
    method: "post",
    data: data
  }).then(createSuccess);
}

export function deleteAddress(pk) {
  return axios({
    url: API.Address + `${pk}/`,
    method: "delete"
  })
    .then(deleteSuccess)
    .catch(deleteFailed);
}

export function getSkills(parameter) {
  return axios({
    url: API.Skills,
    method: "get",
    params: parameter
  });
}

export function updateSkill(pk, data) {
  return axios({
    url: API.Skills + `${pk}/`,
    method: "put",
    data: data
  }).then(updateSuccess);
}

export function createSkill(data) {
  return axios({
    url: API.Skills,
    method: "post",
    data: data
  }).then(createSuccess);
}

export function deleteSkill(pk) {
  return axios({
    url: API.Skills + `${pk}/`,
    method: "delete"
  })
    .then(deleteSuccess)
    .catch(deleteFailed);
}

export function getWorkTimes(parameter) {
  return axios({
    url: API.WorkTimes,
    method: "get",
    params: parameter
  });
}

export function updateWorkTime(pk, data) {
  return axios({
    url: API.WorkTimes + `${pk}/`,
    method: "put",
    data: data
  }).then(updateSuccess);
}

export function createWorkTime(data) {
  return axios({
    url: API.WorkTimes,
    method: "post",
    data: data
  }).then(createSuccess);
}

export function deleteWorkTime(pk) {
  return axios({
    url: API.WorkTimes + `${pk}/`,
    method: "delete"
  })
    .then(deleteSuccess)
    .catch(deleteFailed);
}
