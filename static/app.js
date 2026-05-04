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


async function sendIpInput() {
  const input = document.getElementById("ip-input");
  if (!input) return;

  const ip = input.value;

  try {
    const response = await fetch("/api/ip-input", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ ip: ip })
    });

    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const result = await response.json();
    console.log(result);

  } catch (error) {
    console.error(error.message);
  }
}