import notification from "ant-design-vue/es/notification";
import message from "ant-design-vue/es/message";

export const API = {
  Generate: "auth/phone/generate/",
  Validate: "auth/phone/validate/",
  EmailValidate: "auth/email/validate/",
  Info: "users/info/",
  Logout: "users/logout/",
  Users: "users/",
  Groups: "groups/",
  Permissions: "permissions/",
  Contracts: "contracts/",
  Address: "address/",
  Skills: "skills/",
  WorkTimes: "worktimes/",
  Images: "images/",
  Orders: "orders/",
  Comments: "comments/",
  Faqs: "faqs/",
  Apps: "apps/",
  Applications: "applications/"
};

export function updateSuccess(res) {
  notification.success({
    message: "Update Success"
  });
  return res;
}

export function updateFailed(error) {
  message.error("Update Failed!");
  throw error;
}

export function createSuccess(res) {
  notification.success({
    message: "Create Success"
  });
  return res;
}

export function createFailed(error) {
  message.error("Create Failed!");
  throw error;
}

export function uploadSuccess(res) {
  notification.success({
    message: "Upload Success"
  });
  return res;
}

export function uploadFailed(error) {
  message.error("Upload Failed!");
  throw error;
}

export function deleteSuccess(res) {
  notification.success({
    message: "Delete Success"
  });
  return res;
}

export function deleteFailed(error) {
  message.error("Delete Failed!");
  throw error;
}
