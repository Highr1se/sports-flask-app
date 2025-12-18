window.addEventListener("load", () => {
  document.querySelectorAll(".bar-fill").forEach((bar) => {
    const w = bar.getAttribute("data-width") || "0";
    setTimeout(() => {
      bar.style.width = `${w}%`;
    }, 120);
  });
});