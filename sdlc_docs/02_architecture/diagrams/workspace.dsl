workspace "Research CSV Cleaner" "Local research CSV validation architecture" {
    model {
        researcher = person "Researcher" "Validates experiment data."
        cleaner = softwareSystem "Research CSV Cleaner" "Validates local research CSV files." {
            cli = container "CLI Application" "Runs local command-line CSV validation." "Python"
            streamlit = container "Streamlit Interface" "Runs local upload, preview, count, and download workflow." "Python + Streamlit"
        }
        researcher -> cleaner "Validates experiment data"
        researcher -> cli "Uses command line"
        researcher -> streamlit "Uses local interface"
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
