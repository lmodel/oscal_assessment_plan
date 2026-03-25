package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Root wrapper for an OSCAL Assessment Plan document.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AssessmentPlanDocument extends OscalDocument {

  private AssessmentPlan assessment-plan;

}