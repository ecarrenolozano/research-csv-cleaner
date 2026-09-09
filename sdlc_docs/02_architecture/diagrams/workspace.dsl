workspace "Research CSV Cleaner" "Local research CSV cleaning architecture" {
    model {
        researcher = person "Researcher" "Cleans experiment data."
        cleaner = softwareSystem "Research CSV Cleaner" "Cleans local research CSV files." {
            cli = container "CLI Application" "Processes a local CSV cleaning run." "Python"
        }
        researcher -> cleaner "Cleans experiment data"
        researcher -> cli "Cleans experiment data via CLI"
    }
    views {
        systemContext cleaner "SystemContext" {
            include *
            autoLayout lr
        }
        container cleaner "Containers" {
            include *
            autoLayout lr
        }
        theme default
    }
}
