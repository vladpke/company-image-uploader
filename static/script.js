document.addEventListener("DOMContentLoaded", function () {
  const imageTypeRadios = document.querySelectorAll('input[name="image_type"]');
  const fileInput = document.getElementById("files");
  const uploadBtn = document.getElementById("upload-btn");
  const fileNamesDisplay = document.getElementById("file-names");
  const fileError = document.getElementById("file-error");

  const allowedExtensions = window.ALLOWED_EXTENSIONS || [];

  function isAllowedFile(filename) {
    const ext = filename.toLowerCase().split(".").pop();
    return allowedExtensions.includes(`.${ext}`);
  }

  function updateState() {
    const selectedType = Array.from(imageTypeRadios).some(r => r.checked);
    const files = fileInput.files;
    const hasFiles = files && files.length > 0;

    let allFilesAllowed = true;
    let invalidFiles = [];

    if (hasFiles) {
      Array.from(files).forEach(file => {
        if (!isAllowedFile(file.name)) {
          allFilesAllowed = false;
          invalidFiles.push(file.name);
        }
      });
    }

    // Show/hide error message
    if (!allFilesAllowed) {
      fileError.textContent = `These file(s) are not allowed: ${invalidFiles.join(", ")}`;
      fileError.style.display = "block";
    } else {
      fileError.textContent = "";
      fileError.style.display = "none";
    }

    fileInput.disabled = !selectedType;
    const fileLabel = document.getElementById("file-label");
    if (fileLabel) {
      if (!selectedType) {
        fileLabel.classList.add("disabled");
      } else {
        fileLabel.classList.remove("disabled");
      }
    }

    uploadBtn.disabled = !(selectedType && hasFiles && allFilesAllowed);

    // Show selected file names
    if (hasFiles) {
      const names = Array.from(files).map(f => f.name).join(", ");
      fileNamesDisplay.textContent = names;
    } else {
      fileNamesDisplay.textContent = "No files selected";
    }
  }

  imageTypeRadios.forEach(radio => {
    radio.addEventListener("change", updateState);
  });

  if (fileInput) {
    fileInput.addEventListener("change", updateState);
  }

  updateState();
});
