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

export function getAddress(parameter) {
  return axios({
    url: api.Address,
    method: "get",
    params: parameter
  });
}

export function updateAddress(pk, data) {
  return axios({
    url: api.Address + `${pk}/`,
    method: "put",
    data: data
  });
}

export function createAddress(data) {
  return axios({
    url: api.Address,
    method: "post",
    data: data
  });
}

export function getSkills(parameter) {
  return axios({
    url: api.Skills,
    method: "get",
    params: parameter
  });
}

export function updateSkill(pk, data) {
  return axios({
    url: api.Skills + `${pk}/`,
    method: "put",
    data: data
  });
}

export function createSkill(data) {
  return axios({
    url: api.Skills,
    method: "post",
    data: data
  });
}

export function getWorkTimes(parameter) {
  return axios({
    url: api.WorkTimes,
    method: "get",
    params: parameter
  });
}

export function updateWorkTime(pk, data) {
  return axios({
    url: api.WorkTimes + `${pk}/`,
    method: "put",
    data: data
  });
}

export function createWorkTime(data) {
  return axios({
    url: api.WorkTimes,
    method: "post",
    data: data
  });
}
