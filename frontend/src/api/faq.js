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

export function getFaqs(parameter) {
  return axios({
    url: API.Faqs,
    method: "get",
    params: parameter
  });
}

export function getFaq(pk) {
  return axios({
    url: API.Faqs + `${pk}/`,
    method: "get"
  });
}

export function updateFaq(pk, data) {
  return axios({
    url: API.Faqs + `${pk}/`,
    method: "put",
    data: data
  })
    .then(updateSuccess)
    .catch(updateFailed);
}

export function createFaq(data) {
  return axios({
    url: API.Faqs,
    method: "post",
    data: data
  })
    .then(createSuccess)
    .catch(createFailed);
}

export function deleteFaq(pk) {
  return axios({
    url: API.Faqs + `${pk}/`,
    method: "delete"
  })
    .then(deleteSuccess)
    .catch(deleteFailed);
}
