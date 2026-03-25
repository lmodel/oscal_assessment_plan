package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  An assessment plan, such as those provided by a FedRAMP assessor.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AssessmentPlan  {

  private String uuid;
  private Metadata metadata;
  private ImportSSP import-ssp;
  private LocalDefinitions local-definitions;
  private TermsAndConditions terms-and-conditions;
  private List<AssessmentSubject> assessment-subjects;
  private AssessmentAssets assessment-assets;
  private ReviewedControls reviewed-controls;
  private List<Task> tasks;
  private BackMatter back-matter;

}