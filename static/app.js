async function getLocalIp() {
  const url = "/api/local-ip";
  const localIpElement = document.getElementById("local_ip");

  if (!localIpElement) {
    return;
  }

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const result = await response.json();
    localIpElement.textContent = result.ip;
  } catch (error) {
    console.error(error.message);
    localIpElement.textContent = "Unable to load IP address.";
  }
}

getLocalIp();
