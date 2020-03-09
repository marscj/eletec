import {
  API,
  deleteSuccess,
  deleteFailed,
  createSuccess,
  createFailed
} from "./index";
import { axios } from "@/utils/request";

export function getComments(parameter) {
  return axios({
    url: API.Comments,
    method: "get",
    params: parameter
  });
}

export function getComment(pk, data) {
  return axios({
    url: API.Comments + `${pk}/`,
    method: "put",
    data: data
  });
}

export function createComment(data) {
  return axios({
    url: API.Comments,
    method: "post",
    data: data
  })
    .then(createSuccess)
    .catch(createFailed);
}

export function deleteComment(pk) {
  return axios({
    url: API.Comments + `${pk}/`,
    method: "delete"
  })
    .then(deleteSuccess)
    .catch(deleteFailed);
}
