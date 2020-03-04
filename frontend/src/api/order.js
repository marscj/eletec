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

export function getOrders(parameter) {
  return axios({
    url: API.Orders,
    method: "get",
    params: parameter
  });
}

export function getOrder(pk) {
  return axios({
    url: API.Orders + `${pk}/`,
    method: "get"
  });
}

export function updateOrder(pk, data) {
  return axios({
    url: API.Orders + `${pk}/`,
    method: "put",
    data: data
  })
    .then(updateSuccess)
    .catch(updateFailed);
}

export function createOrder(data) {
  return axios({
    url: API.Orders,
    method: "post",
    data: data
  })
    .then(createSuccess)
    .catch(createFailed);
}

export function deleteOrder(pk) {
  return axios({
    url: API.Orders + `${pk}/`,
    method: "delete"
  })
    .then(deleteSuccess)
    .catch(deleteFailed);
}
