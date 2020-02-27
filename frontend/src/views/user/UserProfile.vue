<template>
  <div>
    <a-form :label-col="{ span: 5 }" :wrapper-col="{ span: 12 }">
      <a-form-item label="Phone Number" required>
        <a-input> </a-input>
      </a-form-item>
      <a-form-item label="First Name">
        <a-input> </a-input>
      </a-form-item>
      <a-form-item label="Last Name">
        <a-input> </a-input>
      </a-form-item>
      <a-form-item label="Email">
        <a-input> </a-input>
      </a-form-item>
      <a-form-item label="Role">
        <a-select>
          <a-select-option key="1" value="Customer">Customer</a-select-option>
          <a-select-option key="2" value="Staff">Staff</a-select-option>
          <a-select-option key="3" value="Freelancer"
            >Freelancer</a-select-option
          >
        </a-select>
      </a-form-item>
      <a-form-item label="Group">
        <a-select mode="multiple">
          <a-select-option key="1" value="1">1</a-select-option>
        </a-select>
      </a-form-item>
      <a-form-item label="Active">
        <a-checkbox />
      </a-form-item>
      <a-button type="primary" html-type="submit">
        Submit
      </a-button>
    </a-form>
  </div>
</template>

<script>
export default {};
</script>
