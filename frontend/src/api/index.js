import notification from "ant-design-vue/es/notification";

export const API = {
  Generate: "auth/phone/generate/",
  Validate: "auth/phone/validate/",
  Info: "users/info/",
  Logout: "users/logout/",
  Users: "users/",
  Groups: "groups/",
  Permissions: "permissions/",
  Contracts: "contracts/",
  Address: "address/",
  Skills: "skills/",
  WorkTimes: "worktimes/",
  Resource: "resources/"
};

export function updateSuccess(res) {
  notification.success({
    message: "Update Success"
  });
  return res;
}

export function updateFailed(res) {
  notification.error({
    message: "Update Failed!"
  });
  return res;
}

export function createSuccess(res) {
  notification.success({
    message: "Create Success"
  });
  return res;
}

export function createFailed(error) {
  notification.error({
    message: "Create Failed!"
  });
  return error;
}

export function uploadSuccess(res) {
  notification.success({
    message: "Upload Success"
  });
  return res;
}

export function uploadFailed(error) {
  notification.error({
    message: "Upload Failed!"
  });
  return error;
}

export function deleteSuccess(res) {
  notification.success({
    message: "Delete Success"
  });
  return res;
}

export function deleteFailed(error) {
  notification.error({
    message: "Delete Failed!"
  });
  return error;
}
