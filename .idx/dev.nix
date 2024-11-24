{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-24.05";

  packages = [
    pkgs.python311
    pkgs.python311Packages.pip
  ];

  env = {};
  idx = {
    extensions = [
      "ms-python.python"
      "amazonwebservices.amazon-q-vscode"
      "gitHub:vscode-github-actions"
      "ms-python.black-formatter"
      "wakatime.vscode-wakatime"
    ];

    # Enable previews
    previews = {
      # enable = true;
      # previews = {
      #   web = {
      #     command = ["python" "manage.py" "runserver"];
      #     manager = "web";
      #     env = {
      #       PORT = "$PORT";
      #     };
      #   };
      # };
    };

    # Workspace lifecycle hooks
    workspace = {
      onCreate = {
        install-dependencies = "python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt";
      };
      onStart = {
        # run-backend = "source .venv/bin/activate && python manage.py runserver";
      };
    };
  };
}
