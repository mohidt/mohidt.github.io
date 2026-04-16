document.addEventListener("DOMContentLoaded", () => {
  const siteHeader = document.querySelector(".site-header");
  const navToggle = document.querySelector(".nav-toggle");
  const siteNav = document.getElementById("site-nav");
  const modal = document.getElementById("project-modal");

  if (siteHeader && navToggle && siteNav) {
    const closeNav = () => {
      siteHeader.classList.remove("nav-open");
      navToggle.setAttribute("aria-expanded", "false");
      document.body.classList.remove("menu-open");
    };

    navToggle.addEventListener("click", () => {
      const isOpen = siteHeader.classList.toggle("nav-open");
      navToggle.setAttribute("aria-expanded", String(isOpen));
      document.body.classList.toggle("menu-open", isOpen);
    });

    siteNav.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", closeNav);
    });

    document.addEventListener("click", (event) => {
      if (!siteHeader.contains(event.target) && siteHeader.classList.contains("nav-open")) {
        closeNav();
      }
    });

    window.addEventListener("resize", () => {
      if (window.innerWidth > 1080) {
        closeNav();
      }
    });
  }

  if (!modal) {
    return;
  }

  const closeModalButton = modal.querySelector(".close-modal");
  const modalTitle = document.getElementById("modal-title");
  const modalImg = document.getElementById("modal-img");
  const modalDesc = document.getElementById("modal-description");
  const modalTools = document.getElementById("modal-tools");
  const modalFeatures = document.getElementById("modal-features");
  const modalReflection = document.getElementById("modal-reflection");
  const modalDownload = document.getElementById("modal-download-link");
  const modalDownloadLabel = document.getElementById("modal-download-label");
  const modalBody = modal.querySelector(".modal-body");
  let lastFocusedElement = null;

  const syncModalBodyHeight = () => {
    if (!modalBody) {
      return;
    }

    modalBody.style.height = "";
  };

  const closeModal = () => {
    modal.classList.remove("is-visible");
    modal.setAttribute("aria-hidden", "true");
    document.body.classList.remove("modal-open");
    modalBody.style.height = "";

    if (lastFocusedElement instanceof HTMLElement) {
      lastFocusedElement.focus();
    }
  };

  const openModal = (button) => {
    lastFocusedElement = document.activeElement;

    modalTitle.textContent = button.dataset.title || "";
    modalImg.src = button.dataset.img || "";
    modalImg.alt = button.dataset.title ? `${button.dataset.title} preview` : "Project preview";
    modalDesc.textContent = button.dataset.description || "";
    modalTools.innerHTML = button.dataset.tools || "";
    modalFeatures.innerHTML = button.dataset.features || "";
    modalReflection.textContent = button.dataset.reflection || "";

    const downloadHref = button.dataset.download || "";
    const isExternal = /^https?:\/\//i.test(downloadHref);

    if (downloadHref) {
      modalDownload.style.display = "inline-flex";
      modalDownload.href = downloadHref;
      modalDownloadLabel.textContent = button.dataset.downloadLabel || "Open file";

      if (isExternal) {
        modalDownload.removeAttribute("download");
        modalDownload.setAttribute("target", "_blank");
        modalDownload.setAttribute("rel", "noopener noreferrer");
      } else {
        modalDownload.setAttribute("download", "");
        modalDownload.removeAttribute("target");
        modalDownload.removeAttribute("rel");
      }
    } else {
      modalDownload.style.display = "none";
      modalDownload.removeAttribute("href");
    }

    modal.classList.add("is-visible");
    modal.setAttribute("aria-hidden", "false");
    document.body.classList.add("modal-open");
    requestAnimationFrame(syncModalBodyHeight);
    closeModalButton.focus();
  };

  document.querySelectorAll(".view-details-button").forEach((button) => {
    button.addEventListener("click", (event) => {
      event.preventDefault();
      openModal(button);
    });
  });

  closeModalButton.addEventListener("click", closeModal);

  modal.addEventListener("click", (event) => {
    if (event.target === modal) {
      closeModal();
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && modal.classList.contains("is-visible")) {
      closeModal();
    }
  });

  window.addEventListener("resize", syncModalBodyHeight);

  modalImg.addEventListener("load", syncModalBodyHeight);
});
