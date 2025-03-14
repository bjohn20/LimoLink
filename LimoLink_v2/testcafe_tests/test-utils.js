// test-utils.js
export async function login(t, username, password) {
  await t
    .navigateTo("http://localhost:8000/login/")
    .typeText("#id_username", username)
    .typeText("#id_password", password)
    .click('button[type="submit"]');
}
