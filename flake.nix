{
  description = "A simple CLI that displays random quotes";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    pyproject-nix.url = "github:pyproject-nix/pyproject.nix";
    uv2nix.url = "github:pyproject-nix/uv2nix";
    pyproject-build-systems.url = "github:pyproject-nix/build-system-pkgs";
  };

  outputs = { self, nixpkgs, pyproject-nix, uv2nix, pyproject-build-systems }:
    let
      forAllSystems = nixpkgs.lib.genAttrs [ "x86_64-linux" "aarch64-linux" ];
    in {
      packages = forAllSystems (system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
          python = pkgs.python312;
          
          workspace = uv2nix.lib.workspace.loadWorkspace { workspaceRoot = ./.; };
          overlay = workspace.mkPyprojectOverlay { sourcePreference = "wheel"; };
          
          pythonSet = (pkgs.callPackage pyproject-nix.build.packages {
            inherit python;
          }).overrideScope (pkgs.lib.composeManyExtensions [
            pyproject-build-systems.overlays.default
            overlay
          ]);
        in {
          default = pythonSet.mkVirtualEnv "quote-bot-env" workspace.deps.default;
          quote-bot = self.packages.${system}.default;
        }
      );
    };
}
